import os
from typing import Callable
from context import FileContext

# import ffmpeg

ffmpeg_bin = "ffmpeg"


def traverse(
    dir: str, format: str, func: Callable, var1=None, var2=None, var3=None
) -> None:
    for obj in os.listdir(dir):
        obj_relative_path = os.path.join(dir, obj)
        if not os.path.isfile(obj_relative_path):
            traverse(obj_relative_path, format, func, var1, var2, var3)
        elif obj_relative_path.lower().endswith(format.lower()):
            ctx = FileContext(obj_relative_path)
            func(ctx, var1, var2, var3)


def execute(cmd: str, ctx=None) -> None:
    print("executing cmd:", cmd)
    os.system(cmd)
    ctx.replace_temp_file()


def compress_image(ctx: FileContext, scale, extesion=None, var3=None) -> None:
    ctx.set_format(extesion)
    base, _ = os.path.splitext(ctx.temp_file_name)
    new_file_name = f"{base}.{extesion}"
    cmd = "{0} -i {1} -vf scale={2} -map_metadata 0 {3} -y".format(
        ffmpeg_bin, ctx.original_file_name, scale, new_file_name
    )
    execute(cmd, ctx)


def compress_video(ctx: FileContext, scale, fps, crf) -> None:  # todo: test
    cmd = "{0} -i {1} -vf scale={2} -r {3} -crf {4} -map_metadata 0 {5} -y".format(
        ffmpeg_bin, ctx.original_file_name, scale, fps, crf, ctx.temp_file_name
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
