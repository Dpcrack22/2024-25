<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <body>
                <h2>Usuarios con ID menor a 300</h2>
                <table border="1">
                    <tr>
                        <th>ID</th>
                        <th>Nombre</th>
                    </tr>
                    <xsl:for-each select="bbdd/jos_users[id &lt; 300]">
                        <tr>
                            <td><xsl:value-of select="id"/></td>
                            <td><xsl:value-of select="name"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
