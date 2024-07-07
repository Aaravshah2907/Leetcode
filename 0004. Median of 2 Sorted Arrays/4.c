void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high)
{
    int pivot = arr[low];
    int i = low;
    int j = high;

    while (i < j)
    {
        while (arr[i] <= pivot && i <= high - 1)
            i++;
        while (arr[j] > pivot && j >= low + 1)
            j--;
        if (i < j)
            swap(&arr[i], &arr[j]);
    }
    swap(&arr[low], &arr[j]);
    return j;
}

void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        int partitionIndex = partition(arr, low, high);
        quickSort(arr, low, partitionIndex - 1);
        quickSort(arr, partitionIndex + 1, high);
    }
}

double findMedianSortedArrays(int *nums1, int nums1Size, int *nums2, int nums2Size)
{
    int arr[nums1Size + nums2Size], size = nums1Size + nums2Size, i;
    for (i = 0; i < nums1Size; i++)
        arr[i] = nums1[i];
    for (i = nums1Size; i < size; i++)
        arr[i] = nums2[size - i - 1];
    quickSort(arr, 0, size - 1);
    if (size % 2 == 0)
        return ((arr[size / 2] + arr[size / 2 - 1]) / 2.0);
    else
        return arr[(size - 1) / 2];
}