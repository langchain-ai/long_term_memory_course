example_input = """
Today was a mix of ups and downs. Started the morning feeling energized after my new morning routine, but got a bit overwhelmed with the project deadlines in the afternoon. 

Need to remember to:
- Email Sarah about the client presentation by Thursday
- Schedule dentist appointment
- Pick up groceries for weekend dinner party

Had an interesting thought during my walk - what if we incorporated AI into our customer feedback system? Could potentially automate the initial response and categorization. Would need to research existing solutions first.

Despite the stress, I'm optimistic about where things are heading. The team's really coming together on the new initiative."""

example_output = """
{
    "memories": [
        {
            "memory_type": "SENTIMENT",
            "memory_content": "Mixed emotions with overall optimistic tone. Started energized, experienced afternoon overwhelm with deadlines, but ended positively about team progress. Key phrases: 'energized', 'overwhelmed', 'optimistic', 'team's coming together'"
        },
        {
            "memory_type": "TODO",
            "memory_content": "Email Sarah about the client presentation (Deadline: Thursday)"
        },
        {
            "memory_type": "TODO",
            "memory_content": "Schedule dentist appointment"
        },
        {
            "memory_type": "TODO",
            "memory_content": "Pick up groceries for weekend dinner party"
        },
        {
            "memory_type": "IDEA",
            "memory_content": "Integrate AI into customer feedback system to automate initial response and categorization."
        }
    ]
}"""