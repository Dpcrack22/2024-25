<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <body>
                <h2>Usuarios con ID menor a 200</h2>
                <table border="1">
                    <tr>
                        <th>Username</th>
                    </tr>
                    <xsl:for-each select="bbdd/jos_users[id &lt; 200]">
                        <tr>
                            <td>
                                <span>
                                    <xsl:attribute name="style">
                                        <xsl:choose>
                                            <xsl:when test="id &lt; 100">color: blue;</xsl:when>
                                            <xsl:otherwise>color: green;</xsl:otherwise>
                                        </xsl:choose>
                                    </xsl:attribute>
                                    <xsl:value-of select="username"/>
                                </span>
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
