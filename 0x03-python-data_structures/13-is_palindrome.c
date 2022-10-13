#include <stdio.h>
#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the address of a pointer that points to the head of a node
 * Return: 1 if it is a palindrome 0 otherwise
 */
int is_palindrome(listint_t **head)
{
int i, num1, num2, k, j, count;
listint_t *tmp;
for (i = 0, tmp = *head; tmp; i++, tmp = tmp->next)
;
for (j = 0, count = i / 2, i--; j < count; j++, i--)
{
for (k = num1 = num2 = 0, tmp = *head; tmp; k++, tmp = tmp->next)
{
if (k == j)
{
num1 = tmp->n;
}
if (k == i)
{
num2 = tmp->n;
}
}
if (num1 != num2)
return (0);
}
return (1);
}
