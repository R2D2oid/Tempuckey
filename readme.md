### Tempuckey Dataset
Tempuckey is a temporally labeled database of hockey videos that span over more than 6.5 hours. The dataset is currently annotated with two hockey actions: *faceoff* (509 instances) and *tripping* (356 instances). There are a total of 690 videos clips; where each clip is 27 seconds long in average and contains one or multiple instances of *faceoff* or *tripping* actions. The table below provides a summary of the dataset information.

<img src="https://github.com/R2D2oid/Tempuckey/blob/master/docs/tempuckey_info.png" alt="Tempuckey Dataset Info" width="800"/>

An example *tripping* action from Tempuckey dataset is displayed below. (<span style="color:green">green</span>) indicates frames that belong to the action and (red) indicates frames that do not belong to that action.

<img src="https://github.com/R2D2oid/Tempuckey/blob/master/docs/tempuckey_tripping_example.png" alt="Tripping" width="600"/>

The videos are obtained from NHL hockey broadcasts and they contain camera movement.
The camera shots in the videos can generally be categorized into three settings: (i) close range shot; (ii) medium range shot; and (iii) far range shot. In order to enable measuring the effect of image scale, we have included the zoom settings of individual clips in the annotations. The following image displays examples of the three shot types.

<img src="https://github.com/R2D2oid/Tempuckey/blob/master/docs/tempuckey_three_shots.png" alt="Tripping" width="600"/>

In addition to the visual annotations, Tempuckey dataset includes textual descriptions from the subtitles. It is important to note the textual descriptions are not directly annotated for the actions that they contain. However, the temporal annotations of the visual content and the subtitle timestamps provide an indirect mean to infer whether the description may be referring to an action. The following table provides a few example subtitle sentences.

<img src="https://github.com/R2D2oid/Tempuckey/blob/master/docs/tempuckey_sentence_examples.png" alt="Tripping" width="600"/>


### Repo Structure

- `videos` folder includes some videos that contain a face-off event (positive videos) and some videos that do not contain a face-off (negative videos).
The names of the videos containing face-off events are included in `Tempuckey_ground_truth_batchxx.csv` files along with the `start_frame` and `end_frame` when the face-off starts and ends.

- `all_videos_UNLABELLED` folder contains approximaptely 10K video clips that we obtained by searching through the closed-captioning and locating the snippets that are likely to contain a face-off event. These videos have not been manually reviewed. This large set of videos could potentially be used for self-supervision.

- `labels` folder contains the groupnd truth labels for the videos that have been manually reviewed.

- `feats` folder contains the extracted features for the clips in the `videos` folder.

- `scripts` folder contains scripts that may be handy in the future. scipts to convert csv labels file to json; evaluate the results against the ground truth and make measuremen
ts.

                                                                                                                                                
