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

bool containsDuplicate(int *nums, int numsSize)
{
    int sort = 0;
    for (int i = 0; i < numsSize - 1; i++)
        if (nums[i] >= nums[i + 1])
            sort++;

    if (!sort)
        return false;
    else
        quickSort(nums, 0, numsSize - 1);

    for (int i = 0; i < numsSize - 1; i++)
        if (nums[i] == nums[i + 1])
            return true;
    return false;
}