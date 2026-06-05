first_bad_version = 4

def isBadVersion(version):

    return version >= first_bad_version

def find_first_bad_version(n):

    left = 1
    right = n

    while left < right:

        mid = (left + right) // 2

        if isBadVersion(mid):
            right = mid

        else:
            left = mid + 1

    return left

total_versions = 10

result = find_first_bad_version(total_versions)

print("First Bad Version:", result)