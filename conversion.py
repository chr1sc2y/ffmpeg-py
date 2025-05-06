import os
from typing import Callable
from context import FileContext
from pathlib import Path

# import ffmpeg

ffmpeg_bin = "ffmpeg"


def traverse(
    dir: str, format: str, func: Callable, var1=None, var2=None, var3=None
) -> None:
    directory = Path(dir)
    for obj in directory.iterdir():
        print(obj)
        obj_relative_path = os.path.join(dir, obj)
        if not os.path.isfile(obj_relative_path):
            traverse(obj_relative_path, format, func, var1, var2, var3)
        elif obj_relative_path.lower().endswith(format.lower()):
            ctx = FileContext(obj_relative_path)
            func(ctx, var1, var2, var3)

def execute(cmd: str, ctx=None) -> None:
    print("executing cmd:", cmd)
    os.system(cmd)
    ctx.archive_original_file()
    ctx.rename_temp_file()


def compress_image(ctx: FileContext, scale, extension=None, var3=None) -> None:
    ctx.set_format(extension)
    base, _ = os.path.splitext(ctx.temp_file_name)
    new_file_name = f"{base}.{extension}"
    cmd = "{0} -i {1} -vf scale={2} -map_metadata 0 {3} -y".format(
        ffmpeg_bin, ctx.original_file_name, scale, new_file_name
    )
    execute(cmd, ctx)

# Option:
# -i {1}            # Input file: Specifies the source video file path
# -vf scale={2}     # Video filter: Adjusts the resolution of the video based on the specified scale {2} value
# -r {3}            # Frame rate: Specifies the frame rate of the output video
# -c:v hevc_nvenc   # Video codec: Specifies the use of NVIDIA's hardware-accelerated H.265/HEVC encoder (requires NVIDIA GPU)
# -profile:v main   # Video profile: Sets the HEVC encoding profile to "main" for better compatibility with devices
# -tag:v hvc1       # Video tag: Sets the HEVC tag to "hvc1" which is required for compatibility with Apple devices (iPhone/Mac)
# -cq 23            # Constant Quality factor: Controls the video quality for NVENC encoder.
#                   # For hevc_nvenc, the range is typically 0-51:
#                   # - Lower values (0-18): Higher quality, larger file size
#                   # - Medium values (19-28): Balanced quality and compression
#                   # - Higher values (29-51): Lower quality, smaller file size
# -map_metadata 0   # Metadata: Copies the metadata from the input video (e.g., title, author) to the output file
# {4}               # Output file: Specifies the destination path for the encoded video
# -y                # Overwrite: Automatically overwrites the output file if it already exists without asking for confirmation
def compress_video(ctx: FileContext, scale, fps, var3=None) -> None:
    cmd = "{0} -i {1} -vf scale={2} -r {3} -c:v hevc_nvenc -profile:v main -tag:v hvc1 -cq 23 -map_metadata 0 {4} -y".format(
        ffmpeg_bin, ctx.original_file_name, scale, fps, ctx.temp_file_name
    )
    execute(cmd, ctx)

def compress_rate(ctx: FileContext) -> None:  # todo: test
    video_rate = "8M"
    audio_rate = "128k"
    cmd = "{0} -i {1} -b:v {2} -b:a {3} {4}".format(
        ffmpeg_bin, ctx.original_file_name, video_rate, audio_rate, ctx.temp_file_name
    )
    execute(cmd, ctx)


def convert_webm_to_mp4(
    ctx: FileContext, scale, var2=None, var3=None
) -> None:  # todo: test
    ctx.set_format("mp4")
    cmd = (
        "{0} -i {1} -vf scale={2} -c:v libx264 -pix_fmt yuv420p -crf 18  {3} -y".format(
            ffmpeg_bin, ctx.original_file_name, scale, ctx.temp_file_name
        )
    )
    os.system(cmd)
