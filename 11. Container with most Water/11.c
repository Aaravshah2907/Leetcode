int maxArea(int *height, int heightSize)
{
    int max_quant = 0, quant = 0, left = 0, right = heightSize - 1;

    while (left < right)
    {
        int width = right - left;
        int height_container = height[left] < height[right] ? height[left] : height[right];
        quant = width * height_container;
        max_quant = max_quant < quant ? quant : max_quant;

        height[left] < height[right] ? left++ : right--;
    }
    return max_quant;
}