int thirdMax(int *nums, int numsSize)
{
    int n = numsSize, temp;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (nums[i] < nums[j])
            {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }

    int count = 1, pos;
    if (n < 3)
        return nums[0];
    for (int i = 0; i < n - 1; i++)
    {
        if (nums[i] != nums[i + 1])
            count++;
        if (count == 3)
            return nums[i + 1];
    }
    return nums[0];
}