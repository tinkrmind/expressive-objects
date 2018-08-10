import urllib
import urllib2

def SubmitJob(printerid, jobtype, jobsrc):
  """Submit a job to printerid with content of dataUrl.

  Args:
    printerid: string, the printer id to submit the job to.
    jobtype: string, must match the dictionary keys in content and content_type.
    jobsrc: string, points to source for job. Could be a pathname or id string.
  Returns:
    boolean: True = submitted, False = errors.
  """
  if jobtype == 'pdf':
    b64file = Base64Encode(jobsrc)
    fdata = ReadFile(b64file)
    hsid = True
  elif jobtype in ['png', 'jpeg']
    fdata = ReadFile(jobsrc)
  else:
    fdata = None

  # Make the title unique for each job, since the printer by default will name
  # the print job file the same as the title.

  datehour = time.strftime('%b%d%H%M', time.localtime())
  title = '%s%s' % (datehour, jobsrc)
    """The following dictionaries expect a certain kind of data in jobsrc, depending on jobtype:
    jobtype                jobsrc
    ================================================
    pdf                    pathname to the pdf file
    png                    pathname to the png file
    jpeg                   pathname to the jpeg file
    ================================================
    """
  content = {'pdf': fdata,
             'jpeg': jobsrc,
             'png': jobsrc,
            }
  content_type = {'pdf': 'dataUrl',
                  'jpeg': 'image/jpeg',
                  'png': 'image/png',
                 }
  headers = [('printerid', printerid),
             ('title', title),
             ('content', content[jobtype]),
             ('contentType', content_type[jobtype])]
  files = [('capabilities', 'capabilities', '{"capabilities":[]}')]
  if jobtype in ['pdf', 'jpeg', 'png']:
    files.append(('content', jobsrc, fdata))
    edata = EncodeMultiPart(headers, files, file_type=content_type[jobtype])
  else:
    edata = EncodeMultiPart(headers, files)

  response = GetUrl('%s/submit' % CLOUDPRINT_URL, tokens, data=edata,
                    cookies=False)
  status = Validate(response)
  if not status:
    error_msg = GetMessage(response)
    logger.error('Print job %s failed with %s', jobtype, error_msg)

  return status

SubmitJob('e9a84714-c055-28b9-3250-1fb760f31c82', 'png', 'https://i.imgur.com/Cu8Q2Gb.png')
