#include <openpose/utilities/keypoint.hpp>
#include <openpose/core/keypointScaler.hpp>

namespace op
{
    KeypointScaler::KeypointScaler(const ScaleMode scaleMode) :
        mScaleMode{scaleMode}
    {
    }

    void KeypointScaler::scale(Array<float>& arrayToScale, const double scaleInputToOutput,
                               const double scaleNetToOutput, const Point<int>& producerSize) const
    {
        try
        {
            std::vector<Array<float>> arrayToScalesToScale{arrayToScale};
            scale(arrayToScalesToScale, scaleInputToOutput, scaleNetToOutput, producerSize);
        }
        catch (const std::exception& e)
        {
            error(e.what(), __LINE__, __FUNCTION__, __FILE__);
        }
    }

    void KeypointScaler::scale(std::vector<Array<float>>& arrayToScalesToScale, const double scaleInputToOutput,
                               const double scaleNetToOutput, const Point<int>& producerSize) const
    {
        try
        {
            if (mScaleMode != ScaleMode::OutputResolution)
            {
                // InputResolution
                if (mScaleMode == ScaleMode::InputResolution)
                    for (auto& arrayToScale : arrayToScalesToScale)
                        scaleKeypoints(arrayToScale, float(1./scaleInputToOutput));
                // NetOutputResolution
                else if (mScaleMode == ScaleMode::NetOutputResolution)
                    for (auto& arrayToScale : arrayToScalesToScale)
                        scaleKeypoints(arrayToScale, float(1./scaleNetToOutput));
                // [0,1]
                else if (mScaleMode == ScaleMode::ZeroToOne)
                {
                    const auto scale = float(1./scaleInputToOutput);
                    const auto scaleX = scale / ((float)producerSize.x - 1.f);
                    const auto scaleY = scale / ((float)producerSize.y - 1.f);
                    for (auto& arrayToScale : arrayToScalesToScale)
                        scaleKeypoints(arrayToScale, scaleX, scaleY);
                }
                // [-1,1]
                else if (mScaleMode == ScaleMode::PlusMinusOne)
                {
                    const auto scale = float(2./scaleInputToOutput);
                    const auto scaleX = (scale / ((float)producerSize.x - 1.f));
                    const auto scaleY = (scale / ((float)producerSize.y - 1.f));
                    const auto offset = -1.f;
                    for (auto& arrayToScale : arrayToScalesToScale)
                        scaleKeypoints(arrayToScale, scaleX, scaleY, offset, offset);
                }
                // Unknown
                else
                    error("Unknown ScaleMode selected.", __LINE__, __FUNCTION__, __FILE__);
            }
        }
        catch (const std::exception& e)
        {
            error(e.what(), __LINE__, __FUNCTION__, __FILE__);
        }
    }
}
