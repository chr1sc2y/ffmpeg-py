import os
from context import FileContext
# import ffmpeg

ffmpeg_bin = "ffmpeg"

def traverse(dir: str, format: str, func, var1 = None, var2 = None, var3 = None) -> None:
    for obj in os.listdir(dir):
        obj_relative_path = os.path.join(dir, obj)
        if not os.path.isfile(obj_relative_path):
            traverse(obj_relative_path, format, func, var1, var2, var3)
        if (obj_relative_path.lower().endswith(format.lower())):
            ctx = FileContext(obj_relative_path)
            func(ctx, var1, var2, var3)

def execute(cmd : str, replace_flag : bool = False, ctx = None) -> None:
    print("executing cmd:", cmd)
    os.system(cmd)
    if replace_flag:
        os.replace(ctx.temp_file, ctx.original_file)

def compress_video(ctx: FileContext, scale, fps, crf) -> None:
    cmd = "{0} -i {1} -vf scale={2} -r {3} -crf {4} -map_metadata 0 {5} -y".format(ffmpeg_bin, ctx.original_file_cmd, scale, fps, crf, ctx.temp_file_cmd)
    execute(cmd, True, ctx)

def compress_image(ctx: FileContext, scale, var2 = None, var = None) -> None:
    cmd = "{0} -i {1} -vf scale={2} -map_metadata 0 {3} -y".format(ffmpeg_bin, ctx.original_file_cmd, scale, ctx.temp_file_cmd)
    execute(cmd, True, ctx)

def compress_rate(ctx: FileContext) -> None:
    video_rate = "8M"
    audio_rate = "128k"
    cmd = "{0} -i {1} -b:v {2} -b:a {3} {4}".format(ffmpeg_bin, ctx.original_file_cmd, video_rate, audio_rate, ctx.temp_file_cmd)
    execute(cmd, True, ctx)
