import sys
import pexpect
import errno

from moulinette.core import MoulinetteError
from moulinette.utils.log import getActionLogger

class Mdadm(object):
    def __init__(self):
        pass

    def create(self, device, level, devices_list, name = None, chunk = None, force = False):
        errors = []
        can_continue = False

        args = ['--create', device]
        if chunk:
            args += ['-c', chunk]
        if name:
            args += ['-N', name]

        args += ['-l', level, '-n', str(len(devices_list))]
        args += devices_list
        self.child = pexpect.spawn('mdadm', args)
        self.child.logfile = sys.stdout

        try:
            errors = self._parse_errors([])
            if self.child.after is not pexpect.EOF and self.child.after.strip() == 'Continue creating array?':
                can_continue = True
                if force:
                    self.child.sendline('Y')
                    self.child.expect('Y\r\n')
                    result = self._parse_errors([])
                    ret = self.child.wait()
                    return { 'warnings': errors, 'result': result, 'success': True if ret == 0 else False }
        except(pexpect.EOF):
            pass

        return { 'errors': errors, 'can_continue': can_continue }

    def _parse_errors(self, errors):
        if self.child.expect(['^mdadm:[^\r]+\r\n', pexpect.EOF, 'Continue creating array\? ']) == 0:
            error = self.child.after.strip()
            if self.child.expect(['\s+[^\r]+\r\n', pexpect.EOF]) == 0:
                error += ' - ' + self.child.after.strip()
            errors.append(error)
            return self._parse_errors(errors)
        return errors

def part_raid_create(device, level, devices, force=False, auth = None):
    try:
        mdadm = Mdadm()
        ret = mdadm.create(device=device, level=level, devices_list=devices, force=force)
        return ret
    except Exception as e:
        raise MoulinetteError(errno.EIO, e.message)
