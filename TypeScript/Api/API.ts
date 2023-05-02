import axios, { AxiosResponse } from "axios";

/**
 * Class API
 */
export default class API {
  private apiUrl: any;

  constructor() {
    this.apiUrl = process.env.API_URL;
  }

  // Create
  public async create(data: any): Promise<AxiosResponse> {
    const response = await axios.post(this.apiUrl, data);
    return response;
  }

  // Read by id
  public async get(id: number): Promise<AxiosResponse> {
    const response = await axios.get(`${this.apiUrl}/${id}`);
    return response;
  }

  // Read by slug
  public async getBySlug(slug: string): Promise<AxiosResponse> {
    const response = await axios.get(`${this.apiUrl}/${slug}`);
    return response;
  }

  // Update
  public async update(id: number, data: any): Promise<AxiosResponse> {
    const response = await axios.put(`${this.apiUrl}/${id}`, data);
    return response;
  }

  // Delete
  public async delete(id: number): Promise<AxiosResponse> {
    const response = await axios.delete(`${this.apiUrl}/${id}`);
    return response;
  }
}
