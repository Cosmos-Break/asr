private void MakeRequests()
{
	HttpWebResponse response;

	if (Request_workingenv1_bosc_cn_3601(out response))
	{
		response.Close();
	}
}

private bool Request_workingenv1_bosc_cn_3601(out HttpWebResponse response)
{
	response = null;

	try
	{
		HttpWebRequest request = (HttpWebRequest)WebRequest.Create("https://workingenv1.bosc.cn:3601/mgw.htm");

		request.Headers.Add("x-mgs-encryption", @"1");
		request.Headers.Add("AppId", @"65854C1021501");
		request.Headers.Add("WorkspaceId", @"product");
		request.Headers.Add("productId", @"65854C1021501_IOS");
		request.Accept = "*/*";
		request.Headers.Add("productVersion", @"10.1.68.27cp0312110000");
		request.Headers.Set(HttpRequestHeader.AcceptLanguage, "zh-CN,zh-Hans;q=0.9");
		request.Headers.Set(HttpRequestHeader.AcceptEncoding, "gzip, deflate, br");
		request.Headers.Add("Operation-Type", @"iom.wa.com.bos.wa.manger.mobile.insertWorkData.biz.ext");
		request.Headers.Add("Platform", @"IOS");
		request.Headers.Add("UniformGateway", @"https://workingenv1.bosc.cn:3601/mgw.htm");
		request.UserAgent = "ShangHangEWork/1 CFNetwork/1335.0.3 Darwin/21.6.0";
		request.KeepAlive = true;
		request.Headers.Add("Ts", @"OCGcKcE");
		request.ContentType = "application/json";
		request.Headers.Set(HttpRequestHeader.Cookie, @"JSESSIONID=fOEQkywi7y7Slldhvj97xAalA9TrxvXubTUtiCa7Eh88VODDg7gE!1526488717; ROUTEID=.server2");
		request.Headers.Add("Sign", @"363f012cf6542aa114d41dd5987444ed");

		request.Method = "POST";
		request.ServicePoint.Expect100Continue = false;

		string body = @"AwAAIQPCbjsx0BDn/AXJcuPGJs/lxzUYkxV7YMCOGUp92SUXVg0AAWAGZAt/25FqfRBoOChlgiFT4CiLHWcBU0QHpH5Wtg9eXBwaT1UFp4UM9HrcZwUsqNqhZS2Biyx9sWevBOyX288nnmDyvhQxSQT2dKE/BZ2VaXVahwASVmNKQpOCUnE86xE6SgDVA1Lygkm/fBcyO+CUutQEngs1sV+SgdQ9URQ9Xyy7Wv7XN2qfGlvEJzCY/a3NPOpy7pfo8o0Cu2nrP5o3XZVqBAaA7pOX0pOdON7pS7KAae9S00ZePSjWaNR6rfHqqRNub0w+BgJjsECASlpyBKA6r0gCEjBo6Rolg6B02t0h1Q2llZm4N6Mbvr8R+0fcriF2sCxTN/MRdwyTZEfDFnWy66AudbqxPDDSqa9Qd11lV7FDWPMWgi3ywFZwNcPTHZLdJBC3CpHitO1ictURgmVGEr8KrvhnVfvjQt3RLDKmb4xO8zYnZJnkcuxsdTNeoOPcNU4nVXoD5uuY2TFn";
		byte[] postBytes = Convert.FromBase64String(body);
		request.ContentLength = postBytes.Length;
		Stream stream = request.GetRequestStream();
		stream.Write(postBytes, 0, postBytes.Length);
		stream.Close();

		response = (HttpWebResponse)request.GetResponse();
	}
	catch (WebException e)
	{
		if (e.Status == WebExceptionStatus.ProtocolError) response = (HttpWebResponse)e.Response;
		else return false;
	}
	catch (Exception)
	{
		if(response != null) response.Close();
		return false;
	}

	return true;
}