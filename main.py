def medians(nums1, nums2):
    ls = sorted(map(int, list(nums1.split() + nums2.split())))
    print(ls)

    if len(ls) % 2 == 0:
        median = (ls[int(len(ls) // 2) ] + ls[int(len(ls) // 2) - 1]) / 2
    else:
        median = ls[int(len(ls) // 2)]

    return median

nums1 = input()
nums2 = input()

print(medians(nums1, nums2))
