# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QuickStepGeobia
                                 A QGIS plugin
 Accuracy assessment of object-based image classification - GEOBIA
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-03-06
        copyright            : (C) 2021 by Salomón Einstein, Ivan Lizarazo
        email                : seramirezf@correo.udistrital.edu.co, ializarazos@unal.edu.co
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load QuickStepGeobia class from file QuickStepGeobia.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .quickstepgeobia import QuickStepGeobia
    return QuickStepGeobia(iface)
