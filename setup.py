from setuptools import setup, Extension

setup(
    name="report-theme-assets",
    version="1.2.0",
    description="Shared report theme assets",
    ext_modules=[Extension("report_theme_assets", ["report_theme_assets.c"], extra_compile_args=["-arch", "arm64"])],
)
