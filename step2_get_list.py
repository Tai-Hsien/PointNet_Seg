# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:25:39 2018

@author: chlian
"""
import numpy as np
import os

if __name__ == '__main__':

    data_path = './augmentation_vtk_data/'
    output_path = './'
    num_augmentations = 20
    train_size = 0.8

    for i_cv in range(1, 2):
        
      if i_cv == 1:
        #6-fold cross-validation #1
        sample_list = list(range(1, 31))
        
        idx = int(np.round(train_size*len(sample_list)))
        train_list, val_list = np.split(sample_list, [idx])
        #test list: 31--36

      elif i_cv == 2:
        #6-fold cross-validation #2
        sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 31, 32, 33, 34, 35, 36]
        idx = int(np.round(train_size*len(sample_list)))
        train_list, val_list = np.split(sample_list, [idx])
        #test list: 25--30

      elif i_cv == 3:
        #6-fold cross-validation #3
        sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        idx = int(np.round(train_size*len(sample_list)))
        train_list, val_list = np.split(sample_list, [idx])
        #test list: 19--24

      elif i_cv == 4:
        #6-fold cross-validation #4
        sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        idx = int(np.round(train_size*len(sample_list)))
        train_list, val_list = np.split(sample_list, [idx])
        #test list: 13--18

      elif i_cv == 5:
        #6-fold cross-validation #5
        sample_list = [1, 2, 3, 4, 5, 6, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        idx = int(np.round(train_size*len(sample_list)))
        train_list, val_list = np.split(sample_list, [idx])
        #test list: 7--12

      elif i_cv == 6:
        #6-fold cross-validation #6
        sample_list = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        idx = int(np.round(train_size*len(sample_list)))
        train_list, val_list = np.split(sample_list, [idx])
        #test list: 1--6

      #training
      train_name_list = []
      for i_sample in train_list: 
        for i_aug in range(num_augmentations):
          print('Computing Sample: {0}; Aug: {1}...'.format(i_sample, i_aug))
          subject_name = 'A{0}_Sample_0{1}_d.vtp'.format(i_aug, i_sample)
          subject2_name = 'A{0}_Sample_0{1}_d.vtp'.format(i_aug, i_sample+1000)
          train_name_list.append(os.path.join(data_path, subject_name))
          train_name_list.append(os.path.join(data_path, subject2_name))

      with open(os.path.join(output_path, 'train_list_{0}.csv'.format(i_cv)), 'w') as file:
        for f in train_name_list:
          file.write(f+'\n')

      #validation
      val_name_list = []
      for i_sample in val_list: 
        for i_aug in range(num_augmentations):
          print('Computing Sample: {0}; Aug: {1}...'.format(i_sample, i_aug))
          subject_name = 'A{0}_Sample_0{1}_d.vtp'.format(i_aug, i_sample)
          subject2_name = 'A{0}_Sample_0{1}_d.vtp'.format(i_aug, i_sample+1000)
          val_name_list.append(os.path.join(data_path, subject_name))
          val_name_list.append(os.path.join(data_path, subject2_name))

      with open(os.path.join(output_path, 'val_list_{0}.csv'.format(i_cv)), 'w') as file:
        for f in val_name_list:
          file.write(f+'\n')


      print('Round:', i_cv)
      print('# of train:', len(train_name_list))
      print('# of validation:', len(val_name_list))
