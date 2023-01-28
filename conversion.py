import os
from context import FileContext

# Windows
ffmpeg = "C:/Users/Administrator/Downloads/ffmpeg"

def traverse(dir: str, format: str, func) -> None:
    for obj in os.listdir(dir):
        obj_relative_path = os.path.join(dir, obj)
        if not os.path.isfile(obj_relative_path):
            traverse(obj_relative_path, format, func)
        if (obj_relative_path.lower().endswith(format.lower())):
            ctx = FileContext(obj_relative_path)
            func(ctx)

def execute(cmd : str, replace_flag : bool = False, ctx = None) -> None:
    # print("executing cmd:", cmd)
    os.system(cmd)
    if replace_flag:
        os.replace(ctx.temp_file, ctx.original_file)

def convert_to_1080p_30fps(ctx: FileContext) -> None:
    scale ="1920:1080"
    fps = 30
    cmd = "{0} -i {1} -vf scale={2} -r {3} {4} -y".format(ffmpeg, ctx.original_file, scale, fps, ctx.temp_file)
    execute(cmd, True, ctx)


def compress_rate(ctx: FileContext) -> None:
    # for 1080p 60 fps
    video_rate = "8M"
    audio_rate = "128k"
    cmd = "{0} -i {1} -b:v {2} -b:a {3} {4}".format(ffmpeg, ctx.original_file, video_rate, audio_rate, ctx.temp_file)
    execute(cmd, True, ctx)

# todo
# traverse(source_dir, ".webm", convert_webm_to_mp4)
def convert_webm_to_mp4(ctx: FileContext) -> None:
    ctx.set_format("mp4")
    cmd = "{0} -i {1} -crf 1 -c:v libx264 {2} -y".format(ffmpeg, ctx.original_file, ctx.temp_file)
    # execute(cmd, True, ctx)
    execute(cmd, False)
