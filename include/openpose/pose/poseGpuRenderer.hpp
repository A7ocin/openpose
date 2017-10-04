#ifndef OPENPOSE_POSE_POSE_GPU_RENDERER_HPP
#define OPENPOSE_POSE_POSE_GPU_RENDERER_HPP

#include <openpose/core/common.hpp>
#include <openpose/core/gpuRenderer.hpp>
#include <openpose/pose/enumClasses.hpp>
#include <openpose/pose/poseExtractor.hpp>
#include <openpose/pose/poseParameters.hpp>
#include <openpose/pose/poseRenderer.hpp>

namespace op
{
    class OP_API PoseGpuRenderer : public GpuRenderer, public PoseRenderer
    {
    public:
        PoseGpuRenderer(const Point<int>& heatMapsSize, const PoseModel poseModel,
                        const std::shared_ptr<PoseExtractor>& poseExtractor, const float renderThreshold,
                        const bool blendOriginalFrame = true, const float alphaKeypoint = POSE_DEFAULT_ALPHA_KEYPOINT,
                        const float alphaHeatMap = POSE_DEFAULT_ALPHA_HEAT_MAP,
                        const unsigned int elementToRender = 0u);

        ~PoseGpuRenderer();

        void initializationOnThread();

        std::pair<int, std::string> renderPose(Array<float>& outputData, const Array<float>& poseKeypoints,
                                               const float scaleNetToOutput = -1.f);

    private:
        const Point<int> mHeatMapsSize;
        const std::shared_ptr<PoseExtractor> spPoseExtractor;
        // Init with thread
        float* pGpuPose; // GPU aux memory

        DELETE_COPY(PoseGpuRenderer);
    };
}

#endif // OPENPOSE_POSE_POSE_GPU_RENDERER_HPP
