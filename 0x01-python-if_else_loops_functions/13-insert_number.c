#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - adds node to linked list
 * @head: pointer to address of head
 * @number: number to be added
 * Return: pointer if added NULL if not
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *prev;
	listint_t *new;

	current = *head;
	while (number > current->n)
	{
		prev = current;
		current = current->next;
	}

	current = prev;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	if (*head == NULL)
		*head = new;
	else
	{
		new->next = current->next;
		current->next = new;
	}

	return (new);
}
