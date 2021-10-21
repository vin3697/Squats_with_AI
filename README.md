# Squats_with_AI
This project counts the number of squat the person does.


I have used OpenCV and mediapipe library to accomplish this task of counting the numbe of squats.

From mediapipe library I have used feature of pose, from where I got the co-ordinates of my shoulder and knee.

My knee co-ordinate is static in nature and my shoulder co-ordinate is varying (while doing squat)

Now, I have just calculated the euclidean distance between them 
and depending on the distance value I have built the logic which enables me to count the number of squats down by person!!


******** I have taken reference from this guy https://github.com/nicknochnack/MediaPipePoseEstimation ********


https://user-images.githubusercontent.com/92587549/138365121-a4de10cf-d7fa-47b8-a3c5-2fc8a1a9e610.mp4

