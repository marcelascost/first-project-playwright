import os
def test_download_files(page):
    page.goto('https://www.transfernow.net/dl/20260820mMfjFcBE')
    page.pause()
    with page.expect_download() as download_info:
        page.get_by_role('link', name='Baixar o arquivo').click()
        page.locator("iframe[name=\"aswift_5\"]").content_frame.get_by_role("button", name="Fechar anúncio").click()
    download = download_info.value
    file_path = 'stores/download/{download.suggested_filename}'
    download.save_as(file_path)
    assert os.path.exists(file_path), 'not founded'