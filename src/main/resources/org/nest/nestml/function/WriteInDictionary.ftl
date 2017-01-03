<#--
  Generates code that

  @param variable VariableSymbol
-->
${signature("variable")}
<#if variable.isAlias() && aliasInverter.isRelativeExpression(variable.getDeclaringExpression().get())>
  def< ${declarations.printVariableType(variable)} >(__d, "${statusNames.name(variable)}", ${names.getter(variable)}());
</#if>