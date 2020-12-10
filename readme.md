### Tempuckey Dataset
Tempuckey is a temporally labeled database of hockey videos that span over more than 6.5 hours. The dataset is currently annotated with two hockey actions: *faceoff* (509 instances) and *tripping* (356 instances). There are a total of 690 videos clips; where each clip is 27 seconds long in average and contains one or multiple instances of *faceoff* or *tripping* actions. Table \ref{table:tempuckey_info} provides a summary of the dataset information.

The videos are obtained from NHL hockey broadcasts and they contain camera movement.
The camera shots in the videos can generally be categorized into three settings: (i) close range shot; (ii) medium range shot; and (iii) far range shot. In order to enable measuring the effect of image scale, we have included the zoom settings of individual clips in the annotations. 



### Repo Structure

- `videos` folder includes some videos that contain a face-off event (positive videos) and some videos that do not contain a face-off (negative videos).
The names of the videos containing face-off events are included in `Tempuckey_ground_truth_batchxx.csv` files along with the `start_frame` and `end_frame` when the face-off starts and ends.

- `all_videos_UNLABELLED` folder contains approximaptely 10K video clips that we obtained by searching through the closed-captioning and locating the snippets that are likely to contain a face-off event. These videos have not been manually reviewed. This large set of videos could potentially be used for self-supervision.

- `labels` folder contains the groupnd truth labels for the videos that have been manually reviewed.

- `feats` folder contains the extracted features for the clips in the `videos` folder.

- `scripts` folder contains scripts that may be handy in the future. scipts to convert csv labels file to json; evaluate the results against the ground truth and make measuremen
ts.

                                                                                                                                                
