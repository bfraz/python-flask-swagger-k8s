import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.blog.business import create_category, delete_category, update_category
from rest_api_demo.api.blog.serializers import category, category_with_posts
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import Category

log = logging.getLogger(__name__)

ns = api.namespace('blog/categories', description='Operations related to blog categories')


@ns.route('/')
class CategoryCollection(Resource):

    @api.marshal_list_with(category)
    def get(self):
        """
        Returns list of blog categories.
        """
        categories = Category.query.all()
        return categories


@ns.route('/<int:id>')
@api.response(404, 'Category not found.')
class CategoryItem(Resource):

    @api.marshal_with(category_with_posts)
    def get(self, id):
        """
        Returns a foo category with a list of posts.
        """
        return Category.query.filter(Category.id == id).one()


    @api.response(204, 'Category successfully deleted.')
    def delete(self, id):
        """
        Deletes blog category.
        """
        delete_category(id)
        return None, 204
