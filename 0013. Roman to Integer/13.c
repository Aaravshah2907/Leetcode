int val(char c)
{
    switch (c)
    {
    case 'I':
        return 1;
    case 'V':
        return 5;
    case 'X':
        return 10;
    case 'L':
        return 50;
    case 'C':
        return 100;
    case 'D':
        return 500;
    case 'M':
        return 1000;
    }
    return 0;
}

int romanToInt(char *s)
{
    int length = strlen(s);
    int sum = 0, value, previous_value = 0;
    for (--length; length > -1; length--)
    {
        value = val(s[length]);
        (value >= previous_value) ? (sum += value) : (sum -= value);
        previous_value = value;
    }
    return sum;
}