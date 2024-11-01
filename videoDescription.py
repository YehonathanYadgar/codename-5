from google.cloud import videointelligence
import io

def analyze_visual_content(video_path):
    # Initialize the Video Intelligence API client
    client = videointelligence.VideoIntelligenceServiceClient()

    # Read the local video file
    with io.open(video_path, "rb") as video_file:
        input_content = video_file.read()

    # Define the features we want to analyze visually 
    features = [
        videointelligence.Feature.LABEL_DETECTION,
        videointelligence.Feature.SHOT_CHANGE_DETECTION,
        videointelligence.Feature.OBJECT_TRACKING
    ]

    # Start analyzing the video
    operation = client.annotate_video(
        request={
            "features": features,
            "input_content": input_content
        }
    )

    # Wait for the operation to complete
    print("Processing video for visual content...")
    result = operation.result(timeout=300)

    # Process and print the results
    for i, annotation in enumerate(result.annotation_results):
        print(f"Results for video segment {i + 1}")

        # Label annotations for visual scene description
        print("\nScene Descriptions:")
        for label in annotation.segment_label_annotations:
            description = label.entity.description
            for segment in label.segments:
                start_time = segment.segment.start_time_offset.total_seconds()
                end_time = segment.segment.end_time_offset.total_seconds()
                confidence = segment.confidence
                print(f"  {description} from {start_time}s to {end_time}s (confidence: {confidence:.2f})")

        # Shot change detection
        print("\nShot Changes:")
        for shot in annotation.shot_annotations:
            start_time = shot.start_time_offset.total_seconds()
            end_time = shot.end_time_offset.total_seconds()
            print(f"  Shot from {start_time}s to {end_time}s")

        # Object tracking annotations
        print("\nObject Tracking:")
        for obj_annotation in annotation.object_annotations:
            entity = obj_annotation.entity.description
            start_time = obj_annotation.segment.start_time_offset.total_seconds()
            end_time = obj_annotation.segment.end_time_offset.total_seconds()
            confidence = obj_annotation.confidence
            print(f"  Object '{entity}' from {start_time}s to {end_time}s (confidence: {confidence:.2f})")

            # Print object track segments
            for frame in obj_annotation.frames:
                time_offset = frame.time_offset.total_seconds()
                box = frame.normalized_bounding_box
                print(f"    - At {time_offset}s: Bounding box [left: {box.left}, top: {box.top}, right: {box.right}, bottom: {box.bottom}]")

    print("Video analysis completed.")

# Example usage with a local video file
analyze_visual_content("test_vid.mp4")
