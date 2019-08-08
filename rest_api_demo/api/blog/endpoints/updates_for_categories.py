

@ns.route('/')
class CategoryCollection(Resource):

#ADD THE POST

    @api.response(201, 'Category successfully created.')
    @api.expect(category)
    def post(self):
        """
        Creates a new blog category.
        """
        data = request.json
        create_category(data)
        return None, 201
############################

@ns.route('/<int:id>')
@api.response(404, 'Category not found.')
class CategoryItem(Resource):


# ALSO, ADD THE PUT

    @api.expect(category)
    @api.response(204, 'Category successfully updated.')
    def put(self, id):
        """
        Updates a blog category.

        Use this method to change the name of a blog category.

        * Send a JSON object with the new name in the request body.

        ```
        {
          "name": "New Category Name"
        }
        ```

        * Specify the ID of the category to modify in the request URL path.
        """
        data = request.json
        update_category(id, data)
        return None, 205
#############
