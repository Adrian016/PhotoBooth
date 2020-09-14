import os
import re


def main():
    # PhotoManager.move_to_temp(current_dir = '.', temp_dir='./temp')
    idx = PhotoManager.next_index_from_file_dir(file_dir = os.path.join(os.getcwd(), "static", "images"),prefix_filter = 'collage')

class PhotoManager:
    # This class is useful for moving and editing images straight from the camera
    def __init__(self):
        pass

    @classmethod
    def move_to_temp(cls, current_dir = '.', temp_dir='./temp',image_type = '.JPG'):
        files = os.listdir(current_dir)
        idx = 1
        for file in files:
            if file.endswith(image_type):
                print(file)
                os.rename(file,temp_dir +'/'+'photo'+str(idx)+image_type)
                idx += 1

    @classmethod
    def next_index_from_file_names(cls, file_names: [str]) -> str:
        # Return the next index number as string

        # Find length of index string
        idx_length = len(re.findall('\d+', file_names[0])[0])

        # Find next index
        i_max = 1
        for string in file_names:
            s_idx = re.findall('\d+', string)[0]
            i_idx = int(s_idx)
            if i_idx >= i_max:
                i_max = i_idx

            next_idx = i_max + 1

            # Add zero padding
            next_idx = str(next_idx).zfill(idx_length)
        return next_idx

    @classmethod
    def next_index_from_file_dir(cls, file_dir: str, prefix_filter: str) -> str:
        file_names = os.listdir(file_dir)
        file_names = list(filter(lambda x: x.startswith(prefix_filter),file_names))
        next_idx = cls.next_index_from_file_names(file_names)
        return next_idx


if __name__ == '__main__':
    main()