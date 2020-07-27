import cv2
import argparse
import logging
import sys
import numpy as np
sys.path.append('/usr/local/data01/zahra/repos/VideoFeatExtratotor/utils')
from sys_utils import *

def extract_flows_for_dataset(videos_dir, output_dir, method = 'tv1l1'):
    videos = get_files_path(videos_dir)
    video_names = [v.split('/')[-1].split('.')[0] for v in videos]

    for v in video_names:
        video_file = '{}/{}.mp4'.format(videos_dir,v)
        output_path = '{}/{}'.format(output_dir,v)
        create_folder(output_path)

        print(output_path)

        cap = cv2.VideoCapture(video_file)
        out = extract_flows(cap, output_path, method)

def normalize_image(img):
    L = -20
    H = 20

    img = 255*(img-L)/(H-L)
    img[img < 0] = 0 # change values less than zero to zero. as in Charades preprocessing     # flow = max(0,flow)
    img[img > 255] = 255 # change values less than zero to zero. as in Charades preprocessing # flow = min(255,flow)
    img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
    return img

def extract_flows(cap, output_path, method = 'tv1l1'):
    ret, frame1 = cap.read()
    frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    count = 0
    while(cap.isOpened()):
        count += 1
        ret, frame2 = cap.read()
        if frame2 is None:
            break
        try:
            frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        except Exception as e:
            print(e)
            print frame2
        if method == 'tv1l1':
            # extract optical flow using TV L1 method
            optical_flow = cv2.optflow.DualTVL1OpticalFlow_create()
            flow = optical_flow.calc(frame1, frame2, None)
        elif method == 'Farneback':
            # extract optical flow using Farneback method
            flow = cv2.calcOpticalFlowFarneback(frame1, frame2, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        else:
            print('specify the method')
            raise NotImplemented
            return 1 

        flow = normalize_image(flow)

        flow_x = flow[:,:,0]
        flow_y = flow[:,:,1]

        cv2.imwrite('{}/flow_x_{}.jpg'.format(output_path, count), flow_x)
        cv2.imwrite('{}/flow_x_{}.jpg'.format(output_path, count), flow_x)

        frame1 = frame2

    cap.release()
    return 0


if __name__ == '__main__':
        # python main.py --method tv1l1 --videos_dir --output_dir
        parser = argparse.ArgumentParser ()
        parser.add_argument('--method', dest = 'method', default = 'tv1l1', help = 'provide optical flow extraction method (ex. tv1l1, Farneback) ')
        parser.add_argument('--videos_dir', dest = 'videos_dir', default = '/usr/local/data02/zahra/datasets/Tempuckey/videos', help = 'provide the path to data')
        parser.add_argument('--output_dir', dest = 'output_dir', default = '/usr/local/data02/zahra/datasets/Tempuckey/feats/flows', help = 'provide output dir')
        parser.add_argument('--configspath', dest = 'configpath', default = 'config.cfg', help = 'provide config file')
        
        args = parser.parse_args ()
        method = args.method
        videos_dir = args.videos_dir
        output_dir = '{}/{}'.format(args.output_dir, method)
        
        # extract flows
        extract_flows_for_dataset(videos_dir, output_dir, method)
        

