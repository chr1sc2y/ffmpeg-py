import os
from .core import FileContext

# ffmpeg
ffmpeg_bin = "ffmpeg -hide_banner -loglevel warning -stats"


def execute(cmd: str, ctx: FileContext = None) -> bool:
    logging.info("❗️ executing cmd: {0}".format(cmd))
    result = os.system(cmd)
    
    # Check command execution result and output file
    if result == 0 and os.path.exists(ctx.temp_file):
        ctx.archive_original_file()
        # ctx.delete_original_file()
        ctx.rename_temp_file()
        logging.info("✅ succeed: {0}\n\n".format(ctx.original_file_name))
        return True
    else:
        logging.error(f"❌ Failed to process {ctx.original_file_name}, exit code: {result}")
        # Clean up failed temporary file
        if os.path.exists(ctx.temp_file):
            os.remove(ctx.temp_file)
            logging.info(f"🗑️  Cleaned up temp file: {ctx.temp_file}")
        return False


def compress_image(ctx: FileContext, scale, extension=None, reserved=None) -> bool:
    """
    Compress and/or convert image to specified format and resolution.
    
    Args:
        ctx: File context object
        scale: Resolution scale (e.g., "3840:2160", "1920:1080", or "original")
        extension: Target file extension (e.g., "jpg", "png")
        reserved: Reserved parameter for future use
    """
    ctx.set_format(extension)
    base, _ = os.path.splitext(ctx.temp_file_name)
    new_file_name = f"{base}.{extension}"

    scale_param = None
    if scale in [None, "original"]:
        scale_param = "iw:ih"
    else:
        scale_param = scale

    cmd = "{0} -i {1} -vf scale={2} -map_metadata 0 {3} -y".format(
        ffmpeg_bin, ctx.original_file_name, scale_param, new_file_name
    )
    return execute(cmd, ctx)
