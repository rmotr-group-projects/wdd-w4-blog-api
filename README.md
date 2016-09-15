# Blog API

Today we will implement a whole API based on a simple and well-known data model: `Blog`, `Author` and `Entry`.

Even though the data model seems pretty straightforward, it provides most of the possible relationships between models.

Here you have a detail of all the endpoints we will work with:

# API endpoints
![endpoints](http://i.imgur.com/1SWjMRH.png)

## `/blogs` endpoint
![blogs](http://i.imgur.com/TgeQsSm.png)

## `/authors` endpoint
![authors](http://i.imgur.com/OtILkcA.png)

## `/entries` endpoint
![entries](http://i.imgur.com/gyNJNsA.png)

# What you need to do

We will concentrate in building all the CRUD (create, retrieve, update, delete) actions using a RESTful API.

Both full and partial updates must be supported in all three endpoints.

You will notice that `/blogs` endpoint is not tested. You need to implement a test suite including tests for all actions in this endpoint.

The `/authors` endpoint must support text search by `name` field, and must also support `id` ordering.
