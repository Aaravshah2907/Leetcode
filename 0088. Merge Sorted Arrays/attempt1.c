void merge(int *nums1, int nums1Size, int m, int *nums2, int nums2Size, int n)
{
    for (int i = 0; i < n; i++)
        nums1[m++] = nums2[i];

    int sorted = 0;
    for (int a = 0; a < m && !sorted; ++a)
    {
        sorted = 1;
        for (int j = 0; j < m - 1 - a; ++j)
        {
            if (nums1[j] > nums1[j + 1])
            {
                sorted = 0;
                int temp = nums1[j];
                nums1[j] = nums1[j + 1];
                nums1[j + 1] = temp;
            }
        }
    }
}