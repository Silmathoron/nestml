#
# ast_ode_shape.py
#
# This file is part of NEST.
#
# Copyright (C) 2004 The NEST Initiative
#
# NEST is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# NEST is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NEST.  If not, see <http://www.gnu.org/licenses/>.

from pynestml.meta_model.ast_node import ASTNode


class ASTOdeShape(ASTNode):
    """
    This class is used to store shapes.
    Grammar:
        odeShape : 'shape' lhs=variable '=' rhs=expr;
    Attributes:
        lhs = None
        rhs = None
    """

    def __init__(self, lhs, rhs, *args, **kwargs):
        """
        Standard constructor.

        Parameters for superclass (ASTNode) can be passed through :python:`*args` and :python:`**kwargs`.

        :param lhs: the variable corresponding to the shape
        :type lhs: ASTVariable
        :param rhs: the right-hand side
        :type rhs: Union[ASTExpression, ASTSimpleExpression]
        """
        super(ASTOdeShape, self).__init__(*args, **kwargs)
        self.lhs = lhs
        self.rhs = rhs

    def clone(self):
        """
        Return a clone ("deep copy") of this node.

        :return: new AST node instance
        :rtype: ASTInputPort
        """
        dup = ASTOdeShape(lhs=self.lhs.clone(),
         rhs=self.rhs.clone(),
         # ASTNode common attributes:
         source_position=self.source_position,
         scope=self.scope,
         comment=self.comment,
         pre_comments=[s for s in self.pre_comments],
         in_comment=self.in_comment,
         post_comments=[s for s in self.post_comments],
         implicit_conversion_factor=self.implicit_conversion_factor)

        return dup

    def get_variable(self):
        """
        Returns the variable of the left-hand side.
        :return: the variable
        :rtype: ast_variable
        """
        return self.lhs

    def get_expression(self):
        """
        Returns the right-hand side rhs.
        :return: the rhs
        :rtype: ast_expression
        """
        return self.rhs

    def get_parent(self, ast):
        """
        Indicates whether a this node contains the handed over node.
        :param ast: an arbitrary meta_model node.
        :type ast: AST_
        :return: AST if this or one of the child nodes contains the handed over element.
        :rtype: AST_ or None
        """
        if self.get_variable() is ast:
            return self
        if self.get_variable().get_parent(ast) is not None:
            return self.get_variable().get_parent(ast)
        if self.get_expression() is ast:
            return self
        if self.get_expression().get_parent(ast) is not None:
            return self.get_expression().get_parent(ast)
        return None

    def equals(self, other):
        """
        The equals method.
        :param other: a different object.
        :type other: object
        :return: True if equal, otherwise False.
        :rtype: bool
        """
        if not isinstance(other, ASTOdeShape):
            return False
        return self.get_variable().equals(other.get_variable()) and self.get_expression().equals(other.get_expression())
