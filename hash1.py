def two(nums,target):
    dicc = {}
    indx = 0
    for element in nums:
        no = target-element
        if no in dicc:
            return dicc[no],indx
        else:
            dicc[element] = indx
        indx+= 1
    return None
