#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head of list
 * @number: input number
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *runner;
	listint_t *pre;
	listint_t *node;

	node = malloc(sizeof(*node));
	if (!node)
		return (NULL);
	node->n = number;
	node->next = NULL;
	if (!*head || number < (*head)->n)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	if (!(*head)->next)
	{
		if ((*head)->n < number)
			return ((*head)->next = node);
		node->next = *head;
		*head = node;
		return (node);
	}
	pre = runner = *head;
	while ((runner = runner->next))
	{
		if (number < runner->n)
		{
			node->next = runner;
			pre->next = node;
			break;
		}
		if (!runner->next)
		{
			runner->next = node;
			break;
		}
		pre = runner;
	}
	return (node);
}

