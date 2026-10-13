from pathlib import Path
import struct
import zlib
from PIL import Image

INPUT_FILE = Path("challenge.png")
OUTPUT_FILE = Path("final_image.png")

WIDTH = 724
HEIGHT = 850

IDAT_STARTS = [
    33, 65581, 131129, 196689,
    262237, 327785, 393333
]


def read_compressed_data(data):
    compressed = bytearray()

    for pos in IDAT_STARTS:
        if pos + 8 > len(data):
            raise ValueError(f"Chunk at offset {pos} is incomplete")

        length = struct.unpack(">I", data[pos:pos + 4])[0]
        kind = data[pos + 4:pos + 8]

        if kind != b"IDAT":
            raise ValueError(
                f"Expected IDAT at offset {pos}, found {kind!r}"
            )

        end = pos + 8 + length
        if end > len(data):
            raise ValueError(f"IDAT at offset {pos} is truncated")

        compressed.extend(data[pos + 8:end])

    # Recover the DEFLATE stream without validating its Adler-32 trailer.
    return zlib.decompress(bytes(compressed)[2:-4], wbits=-15)


def make_chunk(kind, payload):
    crc = zlib.crc32(kind + payload) & 0xFFFFFFFF
    return (
        struct.pack(">I", len(payload))
        + kind
        + payload
        + struct.pack(">I", crc)
    )


def main():
    if not INPUT_FILE.is_file():
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

    print(f"Reading {INPUT_FILE}...")
    source = INPUT_FILE.read_bytes()
    raw = bytearray(read_compressed_data(source))

    row_size = 1 + WIDTH * 3
    expected_size = HEIGHT * row_size

    print(f"Decompressed bytes: {len(raw)}")
    print(f"Expected for {WIDTH}x{HEIGHT}: {expected_size}")

    if len(raw) < expected_size:
        raise ValueError(
            "Not enough decompressed image data to reconstruct "
            f"{WIDTH}x{HEIGHT}: got {len(raw)}, need {expected_size}"
        )

    # Retain exactly the expected scanlines.
    del raw[expected_size:]

    # Replace invalid PNG filter markers with filter 0.
    # This makes the output structurally valid but cannot restore
    # pixel data that was already corrupted.
    bad_rows = []

    for y in range(HEIGHT):
        offset = y * row_size
        if raw[offset] not in range(5):
            bad_rows.append((y, raw[offset]))
            raw[offset] = 0

    print(f"Invalid filter markers replaced: {len(bad_rows)}")
    if bad_rows:
        print("First affected rows:", bad_rows[:15])

    ihdr = struct.pack(
        ">IIBBBBB", WIDTH, HEIGHT, 8, 2, 0, 0, 0
    )

    png_data = (
        b"\x89PNG\r\n\x1a\n"
        + make_chunk(b"IHDR", ihdr)
        + make_chunk(b"IDAT", zlib.compress(bytes(raw)))
        + make_chunk(b"IEND", b"")
    )

    OUTPUT_FILE.write_bytes(png_data)

    # Verify that the resulting PNG can be fully decoded.
    with Image.open(OUTPUT_FILE) as image:
        image.load()
        print(f"Verified output: {OUTPUT_FILE}")
        print(f"Image dimensions: {image.size}")
        print(f"Image mode: {image.mode}")

    print("Recovery finished.")


if __name__ == "__main__":
    main()
