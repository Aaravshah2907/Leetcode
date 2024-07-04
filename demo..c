/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode *makeNode(int num)
{
    struct ListNode *newNode =
        (struct ListNode *)malloc(sizeof(struct ListNode));
    newNode->val = num;
    newNode->next = NULL;
    return newNode;
}

int sum(struct ListNode *list)
{
    int sum = 0, ctrl = 0;
    while (list->next != NULL)
    {
        sum += list->val * pow(10, ctrl++);
        list = list->next;
    }
    sum += list->val * pow(10, ctrl);
    return sum;
}

struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2)
{
    int sum_numbers = sum(l1) + sum(l2);
    l1->next = NULL;
    struct ListNode *tracker = l1;
    if (sum_numbers == 0)
    {
        struct ListNode *temp = makeNode(sum_numbers);
        tracker->next = temp;
        tracker = tracker->next;
    }
    while (sum_numbers > 0)
    {
        int digit = sum_numbers % 10;
        sum_numbers /= 10;
        struct ListNode *temp = makeNode(digit);
        tracker->next = temp;
        tracker = tracker->next;
    }
    tracker->next = NULL;
    return l1->next;
}