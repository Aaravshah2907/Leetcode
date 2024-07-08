int missingNumber(int *nums, int numsSize)
{
    int min = numsSize + 100, max = 0, zero = 0;
    for (int i = 0; i < numsSize; i++)
    {
        min = (nums[i] < min) ? nums[i] : min;
        max = (nums[i] > max) ? nums[i] : max;
    }
    for (int i = min; i <= max; i++)
    {
        int exist = 0;
        for (int j = 0; j < numsSize; j++)
        {
            if (i == nums[j])
                exist++;
            if (nums[j] == 0)
                zero++;
        }
        if (!exist)
            return i;
    }
    if (zero)
        return max + 1;
    else
        return 0;
}