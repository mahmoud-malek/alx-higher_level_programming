#include "lists.h"

/**
 * insert_node - add node with its number to list
 * @head: head node
 * @number: number assoicated with node
 * Return: pointer to new node or null otherwise
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *old = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (old == NULL || old->n >= number)
	{
		new->next = old;
		*head = new;
		return (new);
	}

	/*Loop through the list. we know that it's sorted*/
	while (old && old->next && old->next->n < number)
		old = old->next;

	/*link the node*/
	new->next = old->next;
	old->next = new;

	return (new);
}
