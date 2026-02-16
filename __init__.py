from .nodes import (
    ActualDenoise,
    ActualDenoiseInverse,
    ActualDenoiseInverseStep,
    ActualDenoiseStep,
)

NODE_CLASS_MAPPINGS = {
    "ActualDenoise": ActualDenoise,
    "ActualDenoiseStep": ActualDenoiseStep,
    "ActualDenoiseInverse": ActualDenoiseInverse,
    "ActualDenoiseInverseStep": ActualDenoiseInverseStep,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ActualDenoise": "Actual Denoise",
    "ActualDenoiseStep": "Actual Denoise (step)",
    "ActualDenoiseInverse": "Actual Denoise Inverse",
    "ActualDenoiseInverseStep": "Actual Denoise Inverse (step)",
}
