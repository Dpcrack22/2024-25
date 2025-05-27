<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <body>
                <h2>Usuarios</h2>
                <table border="1">
                    <tr>
                        <th>Username</th>
                        <th>Password</th>
                        <th>Last Visit Date</th>
                    </tr>
                    <xsl:for-each select="bbdd/jos_users">
                        <tr>
                            <td><xsl:value-of select="username"/></td>
                            <td><xsl:value-of select="password"/></td>
                            <td><xsl:value-of select="lastvisitDate"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
