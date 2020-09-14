import re


def next_index(input_string: str) -> str:
    # Return the next index number as string

    # Find length of index string
    idx_length = len(re.findall('\d+',input_string[0])[0])

    # Find next index
    i_max = 1
    for string in input_string:
        s_idx = re.findall('\d+',string)[0]
        i_idx = int(s_idx)
        if i_idx >= i_max:
            i_max = i_idx

        next_idx = i_max + 1

        # Add zero padding
        next_idx = str(next_idx).zfill(idx_length)
    return next_idx


if __name__ == '__main__':
    input_string = ['collage001', 'collage002', 'collage003', 'collage004']
    print(next_index(input_string))
