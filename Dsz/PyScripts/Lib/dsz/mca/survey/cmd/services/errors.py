# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: errors.py
import mcl.status
ERR_SUCCESS = mcl.status.MCL_SUCCESS
ERR_INVALID_PARAM = mcl.status.framework.ERR_START
ERR_TARGET_NOT_SUPPORTED = mcl.status.framework.ERR_START + 1
ERR_MARSHAL_FAILED = mcl.status.framework.ERR_START + 2
ERR_OPEN_FAILED = mcl.status.framework.ERR_START + 3
ERR_ENUM_FAILED = mcl.status.framework.ERR_START + 4
ERR_NO_ENTRIES = mcl.status.framework.ERR_START + 5
errorStrings = {ERR_INVALID_PARAM: 'Invalid parameter(s)',
   ERR_TARGET_NOT_SUPPORTED: 'Remote target not supported on this platform',
   ERR_MARSHAL_FAILED: 'Marshaling data failed',
   ERR_OPEN_FAILED: 'Failed to open services list',
   ERR_ENUM_FAILED: 'Enumeration of services failed',
   ERR_NO_ENTRIES: 'No services found'
   }