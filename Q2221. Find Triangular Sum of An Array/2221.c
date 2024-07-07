int triangularSum(int *nums, int numsSize)
{
    for (int num = 1; num < numsSize; num++)
        for (int i = 0; i < numsSize - 1; i++)
            nums[i] = (nums[i] + nums[i + 1]) % 10;
    return nums[0];
}