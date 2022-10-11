#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - inserts node in sorted array
 * @head: pointer to the address of a pointer that points to the head of a node
 * @number: number to added onto node
 * Return: returns a pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp, *tmp2;

	new = malloc(sizeof(*new));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;
	if (!(*head))
	{
		*head = new;
		return (new);
	}

	for (tmp = (*head)->next, tmp2 = *head; tmp;
		tmp = tmp->next, tmp2 = tmp2->next)
	{
		if (tmp->n > number)
		{
			tmp2->next = new;
			new->next = tmp;
			return (new);
		}
	}
	tmp2->next = new;
	return (NULL);
}
