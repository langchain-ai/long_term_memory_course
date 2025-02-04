# Long-Term Memory Course

## Motivation 

Memory in LLM applications enables intelligent processing and organization of communication over time. A practical example is an AI email assistant that can effectively triage and respond to emails based on learned patterns and preferences. This course is a step-by-step guide to building an LLM-powered email assistant using LangGraph that 1) gives you an actual application that you can deploy and 2) shows you the different types of memories that you can use in AI applications.

## End result

We'll build an app that looks like this, allowing you to process incoming emails with an AI assistant that can:
- Automatically classify emails (respond, ignore, or notify)
- Draft appropriate responses
- Schedule meetings and manage your calendar
- Learn from your communication patterns over time

![Memory Course App](img/memory_course_email.png)

## Organization of the course

The lessons are shown in the `notebooks` folder, structured as follows:

```
- Lesson 1: Concepts
- Lesson 2: Baseline Email Assistant
- Lesson 3: Adding Semantic Memory
- Lesson 4: Adding Episodic Memory
- Lesson 5: Adding Procedural Memory
- Lesson 6: Deploying the App
```

These give you the conceptual foundations for the app in interactive notebooks for exploration and experimentation. The final code needed to run the resulting application is shown in `src/memory_course/` folder, which can be run as a standalone application using [LangGraph server](https://langchain-ai.github.io/langgraph/concepts/langgraph_server/). 

## Running the Application

TODO