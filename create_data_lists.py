from utils import create_data_lists

#voc07_path = 'data/VOC2007'
voc07_path = 'data/FedeSet'
#voc12_path = 'data/VOC2012'
voc12_path = 'data/Damiset'

if __name__ == '__main__':
    create_data_lists(voc07_path= voc07_path,
                      voc12_path= voc12_path,
                      output_folder='./')
